import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../Provider/appState.dart';

class Diary extends StatefulWidget {
  const Diary({Key? key}) : super(key: key);

  @override
  State<Diary> createState() => _DiaryState();
}

class _DiaryState extends State<Diary> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('한줄 일기'),
        centerTitle: true,
      ),

      body: Consumer<ApplicationState>(
          builder: (context, appState, _){
            appState.getDiary();

            if(appState.noDiary){
              return const Center(
                child: Text("아직 데이터가 없습니다!\n파이보와 더 시간을 보내세요!"),
              );
            }

            else{
              for(int i=0; i<appState.diaries.length; i++){
                return ListView(
                  children: [
                    Row(
                      children: [
                        const Text('One line diary: '),
                        Text(appState.diaries[i].note),
                      ],
                    ),
                  ],
                );
              }
            }

            return const Center(child: Text('ERROR!!'),);
          }
      ),
    );
  }
}
