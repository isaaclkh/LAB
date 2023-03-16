import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:ionicons/ionicons.dart';
import 'package:pibo/Functions/feelIcon.dart';
import 'package:provider/provider.dart';

import '../Provider/appState.dart';

class MonthComponent extends StatefulWidget {

  const MonthComponent({Key? key, required this.date}) : super(key: key);

  final String date;

  @override
  State<MonthComponent> createState() => _MonthComponentState();
}

class _MonthComponentState extends State<MonthComponent> {



  @override
  Widget build(BuildContext context) {

    return Consumer<ApplicationState>(
      builder: (context, appState, _){
        appState.getF(widget.date).then((value) => null);
        appState.getD(widget.date).then((value) => null);
        return Container(
          height: 200,
          child: ListView.builder(
              itemCount: appState.fee.length,
              itemBuilder: (context, index){
                return Padding(
                  padding: const EdgeInsets.all(20),
                  child: Card(
                    elevation: 0.0,
                    child: ListTile(
                      title: Row(
                        children: [
                          FeelIcon().howDoYouFeel(appState.fee[index].feel),
                          const SizedBox(width: 15,),
                          Text(appState.fee[index].feel),
                        ],
                      ),
                      subtitle: appState.noDiary? null : Text(appState.diaries[index].note),
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