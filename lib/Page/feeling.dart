import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Page/home.dart';
import 'package:pibo/Provider/appState.dart';
import 'package:pibo/Provider/userProvider.dart';
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
        title: const Text('월간 감정'),
        centerTitle: true,
      ),

      body: Consumer<ApplicationState>(
        builder: (context, appState, _){
          appState.getFeeling();

          if(appState.noFeel){
            return const Center(
                child: Text("아직 데이터가 없습니다!\n파이보와 더 시간을 보내세요!"),
            );
          }

          else{
            return ListView(
              children: [

                Row(
                  children: [
                    const Text('Feel: '),
                    Text(appState.feelings[0].feel),
                  ],
                ),
                Row(
                  children: [
                    const Text('Date: '),
                    Text(appState.feelings[0].date),
                  ],
                ),

                Row(
                  children: [
                    const Text('Feel: '),
                    Text(appState.feelings[1].feel),
                  ],
                ),
                Row(
                  children: [
                    const Text('Date: '),
                    Text(appState.feelings[1].date),
                  ],
                ),
              ],
            );
          }

          return const Center(child: Text('ERROR!!'),);
        }
      ),
    );
  }
}
