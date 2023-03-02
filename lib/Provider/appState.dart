import 'dart:async';
import 'package:flutter/cupertino.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:pibo/main.dart';

import '../firebase_options.dart';
import 'feelingModel.dart';

class ApplicationState extends ChangeNotifier{
  ApplicationState(){
    init();
  }

  List<Feelings> _feelings = [];
  List<Feelings> get feelings => _feelings;

  Future<void> init() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("감정").snapshots().listen((snapshot) {
      _feelings = [];
      for(final document in snapshot.docs){
        _feelings.add(
          Feelings(
            feel : document.data()['느낌'] as String,
            date : document.data()['날짜'] as String,
          ),
        );
      }
      notifyListeners();
    });
  }
}