import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Page/bibleList.dart';
import 'package:pibo/Page/feeling.dart';
import 'package:pibo/Page/home.dart';
import 'package:pibo/Page/monthly.dart';
import 'package:pibo/Page/pictures.dart';
import 'package:ionicons/ionicons.dart';
import 'package:pibo/Provider/appState.dart';
import 'package:provider/provider.dart';

class BottomNavi extends StatefulWidget {
  const BottomNavi({Key? key}) : super(key: key);

  @override
  State<BottomNavi> createState() => _BottomNaviState();
}

class _BottomNaviState extends State<BottomNavi> {

  int _selectedIndex = 0;
  static const TextStyle optionStyle = TextStyle(
    fontSize: 15,
    color: Colors.white,
  );

  final List<Widget> _widgetOptions = <Widget>[
    const HomePage(),
    const BibleList(),
    const Monthly(),
    const Pictures(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
    ApplicationState().init();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: _widgetOptions.elementAt(_selectedIndex),
      ),

      bottomNavigationBar: BottomNavigationBar(
        selectedLabelStyle: optionStyle,
        unselectedLabelStyle: optionStyle,
        // showUnselectedLabels: true,
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            backgroundColor: Color(0xff7286D3),
            icon: Icon(Ionicons.home_outline),
            label: 'HOME',
          ),
          BottomNavigationBarItem(
            backgroundColor: Color(0xff82AAE3),
            icon: Icon(Ionicons.bookmark_outline),
            label: 'BIBLE',
          ),
          BottomNavigationBarItem(
            backgroundColor: Color(0xff144272),
            icon: Icon(Ionicons.calendar_clear_outline),
            label: 'MONTH',
          ),
          BottomNavigationBarItem(
            backgroundColor: Color(0xff6096B4),
            icon: Icon(Ionicons.image_outline),
            label: 'PHOTO',
          ),
        ],
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
      ),
    );
  }

  @override
  void initState() {
    //해당 클래스가 호출되었을떄
    super.initState();

  }

  @override
  void dispose() {
    super.dispose();
  }
}
