// import 'dart:convert';
// import 'package:flip_card/flip_card.dart';
// import '../Functions/apiServices.dart';
// import 'package:http/http.dart' as http;

import 'package:flutter/material.dart';
import 'package:pibo/Functions/parsingComment.dart';
import 'package:pibo/components/filpCard.dart';

class BiblePage extends StatefulWidget {
  const BiblePage(this.words, this.address, this.comment, {Key? key}) : super(key: key);

  final String words;
  final String address;
  final String comment;
  @override
  State<BiblePage> createState() => _BiblePageState();
}

class _BiblePageState extends State<BiblePage> {

  @override
  Widget build(BuildContext context) {
    String text = widget.words;

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: MediaQuery.of(context).size.height * 0.1,
        title: Text(ParsingComment().parse(widget.address)),
        centerTitle: true,
        backgroundColor: const Color(0xff146C94),
      ),

      body: Center(
        child: SizedBox(
          height: MediaQuery.of(context).size.height,
          width: MediaQuery.of(context).size.width * 0.8,
          child: Column(
            children: [
              const Spacer(flex: 1,),
              Container(
                child: Text(widget.words, style: TextStyle(fontSize: 50),),
              ),
              const SizedBox(height: 100,),
              Container(
                // ignore: prefer_interpolation_to_compose_strings
                child: Text('파이보 : ' + ParsingComment().extractSpecial(widget.comment), style: TextStyle(fontSize: 30,),),
              ),
              const Spacer(flex: 2,),
            ],
          ),
        ),
      ),
    );
  }
}
