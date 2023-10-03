
import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'dart:io';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:provider/provider.dart';
import 'package:udp/udp.dart';

import '../Provider/appState.dart';

class GetFromPibo extends StatefulWidget {
  const GetFromPibo({Key? key}) : super(key: key);

  @override
  State<GetFromPibo> createState() => _GetFromPiboState();
}

class _GetFromPiboState extends State<GetFromPibo> {

  final TextEditingController _textController = TextEditingController();
  String sendText = '';
  String receiveText = '';

  void _open(String msg) {
    setState(() {
      RawDatagramSocket.bind(InternetAddress.anyIPv4, 0)
          .then((RawDatagramSocket socket) {
        print('Sending from ${socket.address.address}:${socket.port}');
        int port = 20001;

        String korean = base64.encode(utf8.encode(msg));

        socket.send(korean.codeUnits,
            InternetAddress("192.168.0.155"), port);
        print(msg);
        print(msg.codeUnits);
      });
    });
  }

  void listen() async {
    // creates a UDP instance and binds it to the first available network
    // interface on port 65000.

    // MULTICAST
    var multicastEndpoint =
    Endpoint.multicast(InternetAddress("192.168.0.155"), port: const Port(20001));

    var receiver = await UDP.bind(multicastEndpoint);

    receiver.asStream().listen((datagram) {
      if (datagram != null) {
        var str = String.fromCharCodes(datagram?.data as Iterable<int>);

        stdout.write(str);
        receiveText = str;
      }
    });


    await Future.delayed(const Duration(seconds:5));

    // receiver.close();
  }

  void _listenToBroadCast() {
    InternetAddress multicastAddress = InternetAddress("192.168.0.155");
    int multicastPort = 20001;
    RawDatagramSocket.bind(InternetAddress.anyIPv4, multicastPort)
        .then((RawDatagramSocket socket){
      print('Datagram socket ready to receive');
      print('${socket.address.address}:${socket.port}');

      socket.joinMulticast(multicastAddress);
      print('Multicast group joined');

      socket.listen((RawSocketEvent e){
        Datagram? d = socket.receive();
        if (d == null) return;

        String message = String.fromCharCodes(d.data).trim();
        print('Datagram from ${d.address.address}:${d.port}: ${message}');
        receiveText = message;
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

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: MediaQuery.of(context).size.height * 0.07,
        backgroundColor: Colors.white,
        title: const Text('Pibo', style: TextStyle(color: Colors.black),),
        centerTitle: false,
        leading: IconButton(
          icon : const Icon(Icons.arrow_back_ios_new, color: Colors.black, size: 20,),
          onPressed: () => Navigator.of(context).pop(),
        ),
        elevation: 0.0,
      ),
      body: Consumer<ApplicationState>(
        builder: (context, appState, _) {
          appState.ttromPibo();
          appState.ffromPibo();
          return Column(
            children: [
              Container(
                height: MediaQuery
                    .of(context)
                    .size
                    .height * 0.2,
                color: Colors.teal,
                child: ListView(
                  children: [
                    const Text('FROM PIBO'),
                    const SizedBox(height: 10,),
                    appState.noFromPibo ? Text("") : Text(
                        appState.fromPibo[0].msg)
                  ],
                ),
              ),
              const Divider(color: Colors.grey),
              Container(
                height: MediaQuery
                    .of(context)
                    .size
                    .height * 0.2,
                color: Colors.tealAccent,
                child: ListView(
                  children: [
                    const Text('TO PIBO'),
                    const SizedBox(height: 10,),
                    appState.noToPibo ? Text("") : Text(
                        appState.toPibo[0].msg)
                  ],
                ),
              ),
              TextField(
                controller: _textController,
                style: const TextStyle(color: Colors.black,),
                //obscureText: true,
                decoration: const InputDecoration(
                  enabledBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.white, width: 1,),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderSide: BorderSide(
                      color: Colors.lightBlueAccent, width: 1,),
                  ),

                  hintText: '대답을 입력해주세요. (ex. 좋아)',
                  hintStyle: TextStyle(color: Colors.grey),
                ),

                // inputFormatters: <TextInputFormatter>[
                //   FilteringTextInputFormatter.allow(
                //     RegExp(r'[a-z|A-Z|0-9|ㄱ-ㅎ|ㅏ-ㅣ|가-힣|ᆞ|ᆢ|ㆍ|ᆢ|ᄀᆞ|ᄂᆞ|ᄃᆞ|ᄅᆞ|ᄆᆞ|ᄇᆞ|ᄉᆞ|ᄋᆞ|ᄌᆞ|ᄎᆞ|ᄏᆞ|ᄐᆞ|ᄑᆞ|ᄒᆞ]'),
                //   ),
                // ],

                onSubmitted: _onSubmit,
              ),
            ],
          );
        }),
    );
  }

  void _onSubmit(String value) async{
    _open(value);
    sendText = value;
    print('sendText : $sendText');
    ApplicationState().addttromPibo(value);
    // await context.read<UserProvider>().addUserName(name);
    // Navigator.pushReplacementNamed(context, '/initial', arguments: name);
    _textController.clear();
  }
}