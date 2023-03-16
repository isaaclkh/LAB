import 'dart:math';

import 'package:calendar_appbar/calendar_appbar.dart';
import 'package:flutter/material.dart';
import 'package:pibo/components/monthComponent.dart';
import 'package:provider/provider.dart';
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
    appState = Provider.of<ApplicationState>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('Monthly'),
        centerTitle: true,
      ),
      body: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            TableCalendar(
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
                  appState.getF(selectedDay.toString().split(" ",)[0]);
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
            const Divider(color: Colors.black),
            Consumer<ApplicationState>(
              builder: (context, appState, _){
                return Container(
                  height: 200,
                  child: ListView.builder(
                    itemCount: appState.fee.length,
                    itemBuilder: (context, index){
                      return Padding(
                        padding: EdgeInsets.all(20),
                        child: Card(
                          elevation: 0.0,
                          child: ListTile(
                            title: Row(
                              children: [
                                Text(appState.fee[index].date),
                                Text(appState.fee[index].feel),
                              ],
                            ),
                          ),
                        ),
                      );
                    }
                  ),
                );
              }
            ),
          ],
        ),
      );
  }
}
