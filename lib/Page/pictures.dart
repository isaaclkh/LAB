import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Provider/appState.dart';
import 'package:pibo/main.dart';
import 'package:provider/provider.dart';

class Pictures extends StatefulWidget {
  const Pictures({Key? key}) : super(key: key);

  @override
  State<Pictures> createState() => _PicturesState();
}

class _PicturesState extends State<Pictures> {
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Consumer<ApplicationState>(
        builder: (context, appState, _){

          appState.getPhoto();

          return GridView.builder(
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 3, //1 개의 행에 보여줄 item 개수
                childAspectRatio: 1 / 1, //item 의 가로 1, 세로 2 의 비율
                mainAxisSpacing: 1, //수평 Padding
                crossAxisSpacing: 1, //수직 Padding
              ),
              itemCount: appState.photos.length,
              itemBuilder: (context, index){

                String name = '$userName${appState.photos[index].time}.jpg';

                return SizedBox(
                  width: 100,
                  height: 100,
                  child: Image.network(appState.photos[index].url, fit: BoxFit.fitHeight,),
                );
              }
          );
        }
      ),
    );
  }
}
