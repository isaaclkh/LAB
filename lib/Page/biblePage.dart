// import 'dart:convert';
// import 'package:flip_card/flip_card.dart';
// import '../Functions/apiServices.dart';
// import 'package:http/http.dart' as http;

import 'package:flutter/material.dart';
import 'package:pibo/components/filpCard.dart';

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

    _backgrounding() {
      return Container(
        decoration: BoxDecoration(color: const Color(0xFFFFFFFF)),
      );
    }

    return Scaffold(
      backgroundColor: Colors.black45,
      appBar: AppBar(
        title: Text(widget.address),
      ),
      
      body: Stack(
        fit: StackFit.expand,
        children: <Widget>[
          _backgrounding(),
          Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Expanded(
                flex: 4,
                child: FilpCard(widget.address, widget.words),
              ),
              Expanded(
                flex: 1,
                child: Container(),
              ),
            ],
          )
        ],
      ),
    );
  }
}
