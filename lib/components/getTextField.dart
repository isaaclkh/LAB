import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pibo/Page/home.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:provider/provider.dart';
import 'dart:io';
import '../main.dart';

class GetTextField extends StatefulWidget {
  const GetTextField({Key? key}) : super(key: key);

  @override
  State<GetTextField> createState() => _GetTextFieldState();

  String getName() => _GetTextFieldState().name;
}

class _GetTextFieldState extends State<GetTextField> {
  String name = '';

  void _open(String msg) {
    setState(() {
      RawDatagramSocket.bind(InternetAddress.anyIPv4, 0)
          .then((RawDatagramSocket socket) {
        print('Sending from ${socket.address.address}:${socket.port}');
        int port = 20001;

        String korean = base64.encode(utf8.encode(msg));

        socket.send(korean.codeUnits,
            InternetAddress("192.168.137.150"), port);
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
            InternetAddress("192.168.137.150"), port);
      });
    });
  }

  final TextEditingController _textController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _textController,
      style: const TextStyle(color: Colors.white,),
      //obscureText: true,
      decoration: const InputDecoration(

        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.white, width: 1, ),
        ),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.lightBlueAccent, width: 1, ),
        ),

        labelText: '이름을 입력해주세요 (ex. 홍길동)',
        labelStyle: TextStyle(color: Colors.white),
      ),

      inputFormatters: <TextInputFormatter>[
        FilteringTextInputFormatter.allow(
          RegExp(
              r'[a-z|A-Z|0-9|ㄱ-ㅎ|ㅏ-ㅣ|가-힣|ᆞ|ᆢ|ㆍ|ᆢ|ᄀᆞ|ᄂᆞ|ᄃᆞ|ᄅᆞ|ᄆᆞ|ᄇᆞ|ᄉᆞ|ᄋᆞ|ᄌᆞ|ᄎᆞ|ᄏᆞ|ᄐᆞ|ᄑᆞ|ᄒᆞ]'
          ),
        ),
      ],

      onSubmitted: _onSubmit,
    );
  }

  void _onSubmit(String value) async{

    if(value == 'test'){
      value = value;
    }
    else if(value.length >= 3){
      value = value.substring(value.length-2);
    }

    setState(() => name = value);
    setState(() => userName = value);
    _open(name);
    await context.read<UserProvider>().addUserName(name);
    Navigator.pushReplacementNamed(context, '/initial', arguments: name);
  }

}