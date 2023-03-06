import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Functions/koreanJongSong.dart';
import 'package:pibo/Page/getUserNamePage.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:pibo/components/categoryButtons.dart';
import 'package:pibo/components/getTextField.dart';
import 'package:provider/provider.dart';

import '../main.dart';

/// 메인 색상
Color primaryColor = const Color.fromARGB(255, 83, 184, 138);

/// 포인트 색상
Color accentColor = const Color.fromARGB(255, 199, 176, 121);

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int currentIndex = 0;
  // @override
  // void initState() async{
  //   // TODO: implement initState
  //   // String _uid = await Provider.of<UserProvider>(context, listen: false).getUid();
  //   // Provider.of<ProductProvider>(context, listen: false).getProducts(_uid);
  //   super.initState();
  // }

  @override
  Widget build(BuildContext context) {
    //String? userName = FirebaseAuth.instance.currentUser?.displayName.toString().substring(1);

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.lightBlueAccent,
        elevation: 0.0,
      ),
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [
                Colors.lightBlueAccent,
                Colors.white,
                Colors.white,
              ]
          ),
        ),
        width: MediaQuery.of(context).size.width,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            const SizedBox(height: 10,),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Spacer(flex: 1,),
                Row(
                  children: [
                    Image.asset('assets/pibo_hi.png', width: 100,),
                    Text(
                      '은쪽이는\n${KoreanJongSong().KoreanLEE(userName)}와 친해지고 싶어',
                      style: const TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                Spacer(flex: 7,),
              ],
            ),

            const SizedBox(height: 40,),

            Container(
              width: MediaQuery.of(context).size.width * 0.9,
              height: 400,
              child: Card(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15),
                ),
                elevation: 4.0,
                child: Column(
                  children: [
                    Spacer(),
                    twoRow(),
                    const SizedBox(height: 20,),
                    secondTwoRow(),
                    Spacer(),
                  ],
                ),
              ),
            ),

            const SizedBox(height: 10,),

            ElevatedButton(
              style: ElevatedButton.styleFrom(
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(20),
                ),
              ),
              onPressed: (){
                //FirebaseAuth.instance.signOut();
                UserProvider().updateCurrentUser("");
                Navigator.pushReplacementNamed(context, '/username');
              },
              child: const Text('나가기'),
            ),

            Spacer(),
          ],
        ),
      ),
    );
  }

  Widget twoRow(){
    return Row(
      children: const [
        Spacer(),
        CategoryButtons(where: '/bibleList', buttonName: '추천 받은\n성경구절', buttonIcon: Icons.book_rounded,),
        Spacer(),
        CategoryButtons(where: '/pictures', buttonName: '은쪽이와\n함께한 사진들', buttonIcon: Icons.camera,),
        Spacer(),
      ],
    );
  }

  Widget secondTwoRow(){
    return Row(
      children: const [
        Spacer(),
        CategoryButtons(where: '/feeling', buttonName: '월간\n감정', buttonIcon: Icons.calendar_month),
        Spacer(),
        CategoryButtons(where: '/diary', buttonName: '한줄\n일기', buttonIcon: Icons.note_alt,),
        Spacer(),
      ],
    );
  }
}