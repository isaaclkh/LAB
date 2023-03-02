import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Page/home.dart';
import 'package:pibo/Provider/appState.dart';
import 'package:pibo/components/getTextField.dart';
import 'package:pibo/main.dart';
import 'package:provider/provider.dart';

import '../Provider/appState.dart';

class Feeling extends StatefulWidget {
  const Feeling({Key? key}) : super(key: key);

  @override
  State<Feeling> createState() => FeelingState();
}

class FeelingState extends State<Feeling> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('월간 감정'),
        centerTitle: true,
      ),

      body: ListView(
        children: [
          Consumer<ApplicationState>(
            builder: (context, appState, _) => Column(
              children: [
                Text(appState.feelings.first.feel),
              ],
            ),
          )
        ],
      ),
    );
  }
}
