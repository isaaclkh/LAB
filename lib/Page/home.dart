import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Functions/koreanJongSong.dart';
import 'package:pibo/components/categoryButtons.dart';
import 'package:provider/provider.dart';

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
      body: Center(
        child: SizedBox(
          width: 330,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              //Text('파이보는 ${KoreanJongSong().KoreanLEE(userName!)}와 친해지고 싶어',),
              const SizedBox(height: 130,),
              twoRow(),
              const SizedBox(height: 100,),
              ElevatedButton(
                onPressed: (){
                  //FirebaseAuth.instance.signOut();
                  Navigator.pushReplacementNamed(context, '/');
                },
                child: Text('로그아웃'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget twoRow(){
    return Row(
      children: const [
        CategoryButtons(where: '/bibleList', buttonName: '추천 받은성경구절', buttonIcon: Icons.book_rounded,),
        Spacer(),
        CategoryButtons(where: '/pictures', buttonName: '사진들', buttonIcon: Icons.camera,),
      ],
    );
  }
}