import 'package:flutter/material.dart';
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
  late dynamic _selectedDay = DateTime.now();
  late dynamic _selectedEvents;
  DateTime today = DateTime.now();

  late String userFeel;
  late String userDate;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('MONTH'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TableCalendar(
            firstDay: DateTime.utc(today.year - 1, today.month, today.day),
            // 사용자가 접근할 수 있는 첫 날짜
            lastDay: DateTime.utc(today.year + 10, today.month, today.day),
            // 사용자가 접근할 수 있는 마지막 날짜
            focusedDay: today,
            // 자동 포커스 된 오늘 날짜
            calendarFormat: _calendarFormat,
            // month , 2 weeks, week
            onFormatChanged: (format) { // month, 2 weeks, week 모드 바꿀 때 상태 변화
              setState(() {
                _calendarFormat = format;
              });
            },
            selectedDayPredicate: (day) { // 오늘이 아닌 다른 날짜를 선택했을 경우 포커스
              return isSameDay(_selectedDay, day);
            },
            onDaySelected: (selectedDay, focusedDay) {
              if (!isSameDay(_selectedDay, selectedDay)) {
                setState(() {
                  _selectedDay = selectedDay;
                  _focusedDay = focusedDay;
                  print(_selectedDay.toString().split(" ",)[0]);
                  //_selectedEvents = _getEventsForDay(selectedDay);
                });
              }
            },
            onPageChanged: (focusedDay) {
              _focusedDay = focusedDay;
              print(focusedDay);
            },
            calendarBuilders: CalendarBuilders( // Custom ui
              dowBuilder: (context, day) {
                if (day.weekday == DateTime.sunday ||
                    day.weekday == DateTime.saturday) {
                  final text = DateFormat.E().format(day);
                  return Center(
                    child: Text(
                      text,
                      style: day.weekday == DateTime.sunday ? const TextStyle(
                          color: Colors.red) : TextStyle(color: Colors.blue),
                    ),
                  );
                }
              },
            ),
          ),
          const Divider(
              color: Colors.black
          ),

          Consumer<ApplicationState>(
              builder: (context, appState, _){
                appState.getF(_selectedDay.toString().split(" ",)[0]);

                if(appState.noF){
                  return const Text('no data');
                }
                else{
                  return Column(children: [Text(appState.fee.first.feel)],);
                }
              }
          ),
        ],
      ),
    );
  }
}
