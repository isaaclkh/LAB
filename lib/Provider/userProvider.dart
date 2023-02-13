import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class UserProvider extends ChangeNotifier{

  UserProvider(){
    init();
  }

  void init() async{

  }

  int idx = 0;

  int getIdx() => idx;
  void setIdx(int _idx){
    idx = _idx;
    notifyListeners();
  }

  CollectionReference users = FirebaseFirestore.instance.collection('users');

  Future<String> getUid() async => await FirebaseAuth.instance.currentUser!.uid;

  Future<void> addUserName(String userName) async{
    await users.doc(userName).set(<String, dynamic>{
      "name" : userName,
    }).then((value){

    }).onError((error, stackTrace) => null);

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

}