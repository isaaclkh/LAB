import 'dart:async';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:flutter/cupertino.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:pibo/main.dart';
import 'package:provider/provider.dart';
import 'package:firebase_storage/firebase_storage.dart' as firebase_storage;

import '../Model/photoModel.dart';
import '../firebase_options.dart';
import '../Model/bibleModel.dart';
import '../Model/diaryModel.dart';
import '../Model/feelingModel.dart';

class ApplicationState extends ChangeNotifier{
  ApplicationState(){
    init();
  }

  // TODO get doc id

  List<Feelings> _feelings = [];
  List<Feelings> get feelings => _feelings;

  List<Feelings> _onlyGood = [];
  List<Feelings> get onlyGood => _onlyGood;

  List<Feelings> _onlyBad = [];
  List<Feelings> get onlyBad => _onlyBad;

  List<Feelings> _onlyNorm = [];
  List<Feelings> get onlyNorm => _onlyNorm;

  List<Feelings> _f = [];
  List<Feelings> get fee => _f;

  bool _noF = true;
  bool get noF => _noF;

  List<Diaries> _diaries = [];
  List<Diaries> get diaries => _diaries;

  List<Bible> _bible = [];
  List<Bible> get bible => _bible;

  List<Photos> _photos = [];
  List<Photos> get photos => _photos;

  bool _noFeel = true;
  bool get noFeel => _noFeel;

  bool _noDiary = true;
  bool get noDiary => _noDiary;

  bool _noBible = true;
  bool get noBible => _noBible;

  bool _noPhoto = true;
  bool get noPhoto => _noPhoto;

  String _last = '';
  String get last => _last;

  bool _noLast = true;
  bool get noLast => _noLast;

  Future<void> init() async{

  }

  Future<void> getFeeling() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("감정").snapshots().listen((snapshot) {

      if(snapshot.docs.isEmpty){
        _noFeel = true;
      }

      else{
        _noFeel = false;
        _feelings = [];

        for(final document in snapshot.docs){
          _feelings.add(
            Feelings(
              feel : document.data()['느낌'] as String,
              date : document.data()['날짜'] as String,
            ),
          );
        }
      }

      notifyListeners();
    });
  }

  Future<void> getF(String date) async {
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
    //print('provider '+date);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("감정").doc(date).snapshots().listen((snapshot) {
      if(snapshot.exists){
        _noF = false;
        _f = [];
        _f.add(
          Feelings(feel: snapshot.get('느낌'), date: snapshot.get('날짜')),
        );
      }
      else{
        _noF = true;
        _f=[];
      }
    });

    notifyListeners();
  }

  Future<void> getDiary() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("일기").snapshots().listen((snapshot) {

      if(snapshot.docs.isEmpty){
        _noDiary = true;
      }

      else{
        _noDiary = false;
        _diaries = [];

        for(final document in snapshot.docs){
          _diaries.add(
            Diaries(
              note : document.data()['내용'] as String,
            ),
          );
        }
      }

      notifyListeners();
    });
  }

  Future<void> getD(String date) async {
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
    //print('provider '+date);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("일기").doc(date).snapshots().listen((snapshot) {
      if(snapshot.exists){
        _noDiary = false;
        _diaries = [];
        _diaries.add( Diaries( note : snapshot.get('내용'), ),
        );
      }
      else{
        _noDiary = true;
        _diaries = [];
      }
    });

    notifyListeners();
  }

  Future<void> getBible() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("성경").snapshots().listen((snapshot) {

      if(snapshot.docs.isEmpty){
        _noBible = true;
      }

      else{
        _noBible = false;
        _bible = [];

        for(final document in snapshot.docs){
          _bible.add(
            Bible(
              address : document.data()['주소'] as String,
              words: document.data()['말씀'] as String,
            ),
          );
        }
      }

      notifyListeners();
    });
  }

  Future<void> getPhoto() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

    FirebaseFirestore.instance.collection("users").doc(userName).collection("사진").snapshots().listen((snapshot) {

      if(snapshot.docs.isEmpty){
        _noPhoto = true;
      }

      else{
        _noPhoto = false;
        _photos = [];

        for(final document in snapshot.docs){
          _photos.add(
            Photos(
              time : document.data()['time'] as String,
              url : document.data()['url'] as String,
            ),
          );
        }
      }

      notifyListeners();
    });

  }

  Future<String> downloadURL(String imgUrl) async {
    String downloadURL = firebase_storage.FirebaseStorage.instance
        .ref()
        .child(imgUrl)
        .getDownloadURL().toString();

    return downloadURL;


    // Within your widgets:
    // Image.network(downloadURL);
  }

  Future<void> getLastDay() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

    FirebaseFirestore.instance.collection("users").doc(userName).snapshots().listen((snapshot) {

      if(snapshot.exists){
        _noLast = false;
        _last = snapshot.get('last');
      }
      else{
        _noLast = true;
      }

      notifyListeners();
    });
  }

  Future<void> initializeCount() async{
    await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
    getFeeling();
    
    _onlyGood = _feelings.where((element) => element.feel.contains('GOOD')).toList();
    _onlyBad = _feelings.where((element) => element.feel.contains('BAD')).toList();
    _onlyNorm = _feelings.where((element) => element.feel.contains('NORMAL')).toList();
  }

}