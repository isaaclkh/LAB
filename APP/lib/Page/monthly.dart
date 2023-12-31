import 'package:flutter/material.dart';
import 'package:pibo/components/monthComponent.dart';
import 'package:table_calendar/table_calendar.dart';
import 'package:intl/intl.dart';

import '../Provider/appState.dart';

class Monthly extends StatefulWidget {
  const Monthly({Key? key}) : super(key: key);

  @override
  State<Monthly> createState() => _MonthlyState();
}

class _MonthlyState extends State<Monthly> {
  CalendarFormat _calendarFormat = CalendarFormat.month;
  late dynamic _focusedDay;
  late dynamic _selectedDay;
  late dynamic _selectedEvents;
  DateTime today = DateTime.now();

  @override
  void initState() {
    setState(() {
      _selectedDay = DateTime.now();
      _focusedDay = DateTime.now();
    });
    super.initState();
  }

  late ApplicationState appState;

  @override
  Widget build(BuildContext context) {
    //appState = Provider.of<ApplicationState>(context);

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: MediaQuery.of(context).size.height * 0.1,
        title: Text('CALENDAR'),
        centerTitle: true,
        backgroundColor: Color(0xff579BB1),
      ),
      body: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(height: 10,),
            Container(
              width: MediaQuery.of(context).size.width * 0.95,
              child: TableCalendar(
                firstDay: DateTime.now().subtract(Duration(days: 365*10 + 2)),
                lastDay: DateTime.now().add(Duration(days: 365*10 + 2)),
                focusedDay: _focusedDay,
                selectedDayPredicate: (day) {
                  return isSameDay(_selectedDay, day);
                },
                onDaySelected: (selectedDay, focusedDay) {
                  setState(() {
                    _selectedDay = selectedDay;
                    _focusedDay = focusedDay;
                  });

                  print(selectedDay.toString().split(" ",)[0]);
                },
                onPageChanged: (focusedDay) {
                  _focusedDay = focusedDay;
                },
                calendarFormat: _calendarFormat,
                onFormatChanged: (format) {
                  setState(() {
                    _calendarFormat = format;
                  });
                },
                calendarBuilders: CalendarBuilders( // Custom ui
                  dowBuilder: (context, day) {
                    if (day.weekday == DateTime.sunday || day.weekday == DateTime.saturday) {
                      final text = DateFormat.E().format(day);
                      return Center(
                        child: Text(
                          text,
                          style: day.weekday == DateTime.sunday ? TextStyle(color: Colors.red) : TextStyle(color: Colors.blue),
                        ),
                      );
                    }
                  },
                ),
              ),
            ),
            const SizedBox(height: 50,),
            const Divider(color: Colors.grey),
            MonthComponent(date: _selectedDay.toString().split(" ",)[0]),
          ],
        ),
      );
  }
}
