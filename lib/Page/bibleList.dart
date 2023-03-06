import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../Provider/appState.dart';

class BibleList extends StatelessWidget {
  const BibleList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('한줄 일기'),
        centerTitle: true,
      ),

      body: Consumer<ApplicationState>(
          builder: (context, appState, _){
            appState.getBible();

            if(appState.noBible){
              return const Center(
                child: Text("아직 데이터가 없습니다!\n파이보와 더 시간을 보내세요!"),
              );
            }

            else{
              for(int i=0; i<appState.bible.length; i++){
                return ListView(
                  children: [
                    // TODO : get doc id and show in text
                    Text(''),
                    Row(
                      children: [
                        const Text('Address: '),
                        Text(appState.bible[i].address),
                      ],
                    ),
                    Row(
                      children: [
                        const Text('Words: '),
                        Text(appState.bible[i].words),
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
