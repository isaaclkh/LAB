import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../components/udpSend.dart';

class Chatting extends StatefulWidget {
  const Chatting({Key? key}) : super(key: key);

  @override
  State<Chatting> createState() => _ChattingState();
}

class _ChattingState extends State<Chatting> {
  List sendTextList = const UDPSend().getSendTextList();
  List receiveTextList = [];
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


      resizeToAvoidBottomInset: true, // resize when keyboard pop up

      body: GestureDetector(
        onTap: () => FocusScope.of(context).requestFocus(FocusNode()),
        child: Column(
          children: [
            Flexible(
              flex: 12,
              child: Container(
                color: Colors.tealAccent,
                child: ListView.builder(
                  itemCount: sendTextList.length + receiveTextList.length,
                  itemBuilder: (context, index){
                    return Column(
                      children: [
                        Container(
                          child: Text(
                            sendTextList[index]
                          ),
                        )
                      ],
                    );
                  }
                ),
              ),
            ),
            Expanded(
              child: Container(
                height: 100,
                decoration: const BoxDecoration(
                  color: Colors.white,
                  boxShadow: [
                    BoxShadow(
                      offset: Offset(0, -3),
                      blurRadius: 6.0,
                      color: Colors.black12,
                    )
                  ]
                ),
                alignment: Alignment.topCenter,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Expanded(
                      child: _buildMessageInput(context),
                    ),
                    SizedBox(
                        height: 59,
                        width: 59,
                        child: RawMaterialButton (
                          fillColor: Colors.teal,
                          elevation: 5.0,
                          child: const Icon(
                            Icons. send,
                            color: Colors.white,
                          ),
                          onPressed: () {
                            UDPSend().submit();
                            sendTextList = const UDPSend().getSendTextList();
                          }
                        ),
                    ),
                 ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  _buildMessageInput(context) => const UDPSend();
  getSendText() {
    String temp;
    temp = UDPSend().getSendText();
    print('temp : $temp');
    sendTextList.add(temp);
  }
}
