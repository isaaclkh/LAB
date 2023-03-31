import 'dart:convert';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import '../Functions/apiServices.dart';

class BiblePage extends StatefulWidget {
  const BiblePage(this.words, this.address, {Key? key}) : super(key: key);

  final String words;
  final String address;
  @override
  State<BiblePage> createState() => _BiblePageState();
}

class _BiblePageState extends State<BiblePage> {
  String? image = '';
  @override
  Widget build(BuildContext context) {
    String text = widget.words;

    return Scaffold(
      backgroundColor: Colors.black45,
      appBar: AppBar(
        title: Text(widget.address),
      ),
      
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Column(
          children: [
            Expanded(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: Container(
                          height: 50,
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4,),
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(12),

                          ),
                          child: Align(
                            alignment:Alignment.center,
                            child: Text('${widget.words}'),),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(
                    width: 300,
                    height: 44,
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.deepPurple,
                        shape: const StadiumBorder(),
                      ),
                      onPressed: () async{
                        // if(widget.words.isNotEmpty){
                        //   print(text);
                        //   image = await Api.generateImage(text);
                        // }
                        // else{
                        //   ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('성경 구절이 없어요')));
                        // }
                        print(text);
                        image = await Api.generateImage(text);
                        print(image);
                      },
                      child: const Text('그리기'),
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              flex: 4,
              child: Container(
                color: Colors.blue,
              ),
            ),
          ],
        ),
      )
    );
  }
}
