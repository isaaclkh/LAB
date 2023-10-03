import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pibo/Page/home.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:provider/provider.dart';
import 'dart:io';
import '../main.dart';

class UDPSend extends StatefulWidget {
  const UDPSend({Key? key}) : super(key: key);



  @override
  State<UDPSend> createState() => _UDPSendState();

  String getName() => _UDPSendState().name;
  String getSendText() => _UDPSendState().sendText;
  List getSendTextList() => _UDPSendState().sendTextList;
  submit() => _UDPSendState()._onSubmit(_UDPSendState().sendText);
}

class _UDPSendState extends State<UDPSend> {
  String name = '';
  String sendText = '';
  List sendTextList = [];

  void _open(String msg) {
    setState(() {
      RawDatagramSocket.bind(InternetAddress.anyIPv4, 0)
          .then((RawDatagramSocket socket) {
        print('Sending from ${socket.address.address}:${socket.port}');
        int port = 20001;

        String korean = base64.encode(utf8.encode(msg));

        socket.send(korean.codeUnits,
            InternetAddress("192.168.137.60"), port);
        print(msg);
        print(msg.codeUnits);
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
            InternetAddress("192.168.137.60"), port);
      });
    });
  }

  final TextEditingController _textController = TextEditingController();
  @override
  Widget build(BuildContext context) {

    return TextField(
      controller: _textController,
      style: const TextStyle(color: Colors.black,),
      // maxLines: null,
      // textInputAction: TextInputAction.newline,
      // keyboardType: TextInputType.multiline,
      // obscureText: true,
      decoration: const InputDecoration(

        enabledBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Colors.grey, width: 1, ),
        ),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.grey, width: 1, ),
        ),

        hintText: '대답을 입력해주세요. (ex. 좋아)',
        hintStyle: TextStyle(color: Colors.grey),
      ),

      // inputFormatters: <TextInputFormatter>[
      //   FilteringTextInputFormatter.allow(
      //     RegExp(
      //         r'[a-z|A-Z|0-9|ㄱ-ㅎ|ㅏ-ㅣ|가-힣|ᆞ|ᆢ|ㆍ|ᆢ|ᄀᆞ|ᄂᆞ|ᄃᆞ|ᄅᆞ|ᄆᆞ|ᄇᆞ|ᄉᆞ|ᄋᆞ|ᄌᆞ|ᄎᆞ|ᄏᆞ|ᄐᆞ|ᄑᆞ|ᄒᆞ]'
      //     ),
      //   ),
      // ],

      onSubmitted: _onSubmit,
    );
  }

  void _onSubmit(String value) async{
    _open(value);
    sendText = _textController.text;
    print('sendText : $sendText');
    sendTextList.add(sendText);
    _textController.clear();
  }

}