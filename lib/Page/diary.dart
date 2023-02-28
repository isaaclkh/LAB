import 'dart:io';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Diary extends StatefulWidget {
  const Diary({Key? key}) : super(key: key);

  @override
  State<Diary> createState() => _DiaryState();
}

class _DiaryState extends State<Diary> {

  void _open() {
    setState(() {
      RawDatagramSocket.bind(InternetAddress.anyIPv4, 0)
          .then((RawDatagramSocket socket) {
        print('Sending from ${socket.address.address}:${socket.port}');
        int port = 20001;
        socket.send('open'.codeUnits,
            InternetAddress("192.168.0.146"), port);
      });
    });
  }

  void _close() {
    setState(() {
      RawDatagramSocket.bind(InternetAddress.anyIPv4, 0)
          .then((RawDatagramSocket socket) {
        print('Sending from ${socket.address.address}:${socket.port}');
        int port = 20001;
        socket.send('close'.codeUnits,
            InternetAddress("192.168.0.146"), port);
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('UDP client test'),
      ),
      body: Center(
        child: Column(

          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,
                padding: EdgeInsets.fromLTRB(40, 20, 40, 20),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20.0)),
              ),

              child: Text("Open",
                style: TextStyle(
                  fontSize: 40,
                ),
              ),

              onPressed: _open,
            ),
            Padding(
              padding: new EdgeInsets.fromLTRB(10, 100, 10, 10),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,
                padding: EdgeInsets.fromLTRB(40, 20, 40, 20),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(20.0)),
              ),

              child: Text("Close",
                style: TextStyle(
                  fontSize: 40,
                ),
              ),

              onPressed: _close,
            ),
          ],
        ),
      ),
    );
  }
}
