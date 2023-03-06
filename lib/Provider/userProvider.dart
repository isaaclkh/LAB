import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

import '../main.dart';

class UserProvider extends ChangeNotifier{

  CollectionReference users = FirebaseFirestore.instance.collection('users');
  CollectionReference uname = FirebaseFirestore.instance.collection('currentUser');

  Future<String> getUid() async => await FirebaseAuth.instance.currentUser!.uid;
  StreamSubscription<DocumentSnapshot>? _userName;
  StreamSubscription<DocumentSnapshot<Object?>>? get getUName => _userName;

  UserProvider(){
    init();
  }

  void init() async{
    _userName = FirebaseFirestore.instance
        .collection("currentUser")
        .doc("VHRiz1RFjGbVMXWB3IP3")
        .snapshots()
        .listen((snapshot){
      if(snapshot.data()!['userName'] != ""){
        _userName = userName as StreamSubscription<DocumentSnapshot<Object?>>?;
      }
      notifyListeners();
    });

  }

  int idx = 0;

  int getIdx() => idx;
  void setIdx(int _idx){
    idx = _idx;
    notifyListeners();
  }


  Future<void> addUserName(String userName) async{
    await users.doc(userName).set(<String, dynamic>{
      "name" : userName,
    }).then((value){
      _userName = userName as StreamSubscription<DocumentSnapshot<Object?>>?;
    }).onError((error, stackTrace) => null);
    notifyListeners();
  }

  Future<void> updateCurrentUser(String UN) async{
    await uname.doc('VHRiz1RFjGbVMXWB3IP3').update(<String, dynamic>{
      "userName" : userName,
    }).then((value){

    }).onError((error, stackTrace) => null);
    notifyListeners();
  }

  Future<void> addUser(User user) async{
    await users.doc(user.uid).set(<String, dynamic>{
      "userId" : user.uid,
      "name" : user.displayName,

    }).then((value){

    }).onError((error, stackTrace) => null);

  }

  Future<void> editUser(User user) async{
    await users.doc(user.uid).update({

    }).then((value){

    }).onError((error, stackTrace) => null);
  }

  Future<void> deleteUser(String uid) async{
    await users.doc(uid).delete();
  }

  Future<void> readUser(String uid) async {
    await users.doc(uid).get().then((value){
      if(!value.exists){
        print("userProvider: no data in the docId");
      }
      else{
        Map<String, dynamic> data = value.data() as Map<String, dynamic>;
        return Text("Name: ${data['name']}");
      }
    });
  }

  Future<void> changeCurrentUser() async{
    _userName = FirebaseFirestore.instance
        .collection("currentUser")
        .doc("VHRiz1RFjGbVMXWB3IP3")
        .snapshots()
        .listen((snapshot){
      if(snapshot.data()!['userName'] != ""){
        _userName = userName as StreamSubscription<DocumentSnapshot<Object?>>?;
      }
      notifyListeners();
    });
  }

}