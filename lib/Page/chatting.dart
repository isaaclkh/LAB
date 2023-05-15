import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Chatting extends StatefulWidget {
  const Chatting({Key? key}) : super(key: key);

  @override
  State<Chatting> createState() => _ChattingState();
}

class _ChattingState extends State<Chatting> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: MediaQuery.of(context).size.height * 0.1,
        title: const Text('Chat With me'),
        centerTitle: true,
        backgroundColor: const Color(0xff146C94),
      ),
    );
  }
}
