import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Provider/productProvider.dart';
import 'package:pibo/components/getTextField.dart';
import 'package:provider/provider.dart';

class Feeling extends StatefulWidget {
  const Feeling({Key? key}) : super(key: key);

  @override
  State<Feeling> createState() => _FeelingState();
}

class _FeelingState extends State<Feeling> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('월간 감정'),
        centerTitle: true,
      ),

      body: ListView(
        children: [
          FutureBuilder(
            future: ProductProvider().getFeeling(GetTextField().getName()),
            builder: (BuildContext context, AsyncSnapshot snapshot){
              return Container(

              );
            },
          )
        ],
      ),
    );
  }
}
