import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../Provider/appState.dart';
import '../Provider/feelingModel.dart';

class MonthComponent extends StatefulWidget {

  const MonthComponent({Key? key, required this.fee}) : super(key: key);

  final List<Feelings> fee;

  @override
  State<MonthComponent> createState() => _MonthComponentState();
}

class _MonthComponentState extends State<MonthComponent> {
  @override
  Widget build(BuildContext context) {
    return Container(
      height: 200,
      child: ListView.builder(
        itemCount: widget.fee.length,
        itemBuilder: (context, index){
          return Padding(
            padding: EdgeInsets.all(20),
            child: Card(
              elevation: 0.0,
              child: ListTile(
                title: Row(
                  children: [
                    Text(widget.fee[index].date),
                    Text(widget.fee[index].feel),
                  ],
                ),
              ),
            ),
          );
        }
      ),
    );
  }
}