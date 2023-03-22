import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../Provider/appState.dart';

class BibleList extends StatelessWidget {
  const BibleList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Consumer<ApplicationState>(
      builder: (context, appState, _){
        appState.getBible();

        return Scaffold(
          appBar: AppBar(
            toolbarHeight: MediaQuery.of(context).size.height * 0.1,
            title: const Text('BIBLE'),
            centerTitle: true,
            backgroundColor: Color(0xff146C94),
          ),

          body: appState.noBible?
                  const Center(
                    child: Text('아직 성경 추천 받은게 없어요\n파이보와 더 친해져보아요 :)'),
                  ):
                  ListView.builder(
                    itemCount: appState.bible.length,
                    itemBuilder: (context, index){
                      return Padding(
                        padding: const EdgeInsets.all(20),
                        child: Card(
                          elevation: 0.0,
                          child: ListTile(
                            title: Text(appState.bible[index].words),
                            subtitle: Text(appState.bible[index].address),
                          ),
                        ),
                      );
                    }
                  ),
          );
      }
    );
  }
}
