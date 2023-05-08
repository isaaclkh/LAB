import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Page/biblePage.dart';
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

                      return Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const SizedBox(height: 10,),
                          Padding(padding: const EdgeInsets.only(left: 30, top: 20, bottom: 5,),
                            child: Text(appState.bibleDates[index], style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 15,),),
                          ),

                          Padding(
                            padding: const EdgeInsets.only(left: 20, right: 20,),
                            child: Card(
                              elevation: 0.0,
                              child: ListTile(
                                title: Text(appState.bible[index].words, overflow: TextOverflow.ellipsis,),
                                subtitle: Text(appState.bible[index].address),
                                onTap: (){
                                  Navigator.push(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context)=> BiblePage(appState.bible[index].words, appState.bible[index].address),
                                    ),
                                  );
                                },
                              ),
                            ),
                          ),
                        ],
                      );
                    }
                  ),
          );
      }
    );
  }
}
