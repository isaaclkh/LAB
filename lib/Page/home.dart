import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:ionicons/ionicons.dart';
import 'package:pibo/Functions/koreanJongSong.dart';
import 'package:pibo/Provider/appState.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:provider/provider.dart';

import '../main.dart';

/// 메인 색상
// Color primaryColor = const Color.fromARGB(255, 83, 184, 138);

/// 포인트 색상
// Color accentColor = const Color.fromARGB(255, 199, 176, 121);

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
        toolbarHeight: MediaQuery.of(context).size.height * 0.1,
        backgroundColor: Colors.white,
        elevation: 0.0,
        leadingWidth: 100,
        leading: IconButton(
          icon: const Icon(Ionicons.log_out_outline, color: Colors.black, size: 30,),
          tooltip: 'Logout',
          onPressed : (){
            UserProvider().updateCurrentUser("");
            Navigator.pushReplacementNamed(context, '/username');
          }
        ),
        actions: [
          Padding(
            padding: EdgeInsets.only(top: 20, right: 20, bottom: 15,),
            child: Container(
              width: 55,
              child: ClipRRect(
                borderRadius: BorderRadius.circular(15),
                child: SizedBox.fromSize(
                  size: Size.fromRadius(48),
                  child: Image.asset('assets/piboAppBar.jpeg', fit: BoxFit.fitWidth,),
                ),
              ),
            ),
          )
        ],
      ),

      body: Container(
        color: Colors.white,
        width: MediaQuery.of(context).size.width,
        child: ListView(
          //mainAxisAlignment: MainAxisAlignment.start,
          children: [
            const SizedBox(height: 20,),
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('나의 행복 지수', style: TextStyle(fontSize: 18, color: Colors.grey.shade600,),),
                const SizedBox(height: 10,),
                Consumer<ApplicationState>(
                    builder: (context, appState, _){
                      appState.initializeCount();

                      if(appState.noFeel){
                        return const Text('아직 데이터가 없어요', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 30,),);
                      }
                      else{
                        return Text('${appState.onlyGood.length/appState.feelings.length * 100}', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 50,),);
                      }
                    }
                ),
              ],
            ),

            const SizedBox(height: 30,),

            Padding(
              padding: const EdgeInsets.only(right: 30, left: 30,),
              child: Container(
                height: 160,
                decoration: BoxDecoration(
                  color: const Color(0xff97DEFF),
                  borderRadius: BorderRadius.circular(50),
                  image: const DecorationImage(
                    image: AssetImage('assets/buttonBackground.png'),
                    opacity: 0.4,
                    fit: BoxFit.cover,
                  ),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    const Spacer(),
                    Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          '${KoreanJongSong().KoreanLEE(userName)}와\n친해지고 싶어',
                          style: const TextStyle(
                            fontSize: 22,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        const SizedBox(height: 5,),
                        Consumer<ApplicationState>(
                            builder: (context, appState, _){
                              appState.getLastDay();

                              if(appState.noLast){
                                return Container();
                              }
                              else{
                                return Text('마지막 날짜 ${appState.last}',
                                  style: TextStyle(fontSize: 15, color: Colors.grey.shade700),);
                              }
                            }
                        ),
                      ],
                    ),
                    const SizedBox(width: 15,),
                    Image.asset('assets/pibo_hi.png', width: 100,),
                    const Spacer(),
                  ],
                ),
              ),
            ),

            const SizedBox(height: 40,),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(
                  width: MediaQuery.of(context).size.width * 0.8,
                  child: const Padding(
                    padding: EdgeInsets.only(left : 8),
                    child: Text(
                      '나의 활동',
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        fontSize: 17,
                      ),
                    ),
                  ),
                )
              ],
            ),

            const SizedBox(height: 18,),

            Consumer<ApplicationState>(
              builder: (context, appState, _){
                appState.initializeCount();

                if(appState.noFeel){
                  return SizedBox(
                    width: MediaQuery.of(context).size.width * 0.8,
                    height: 110,
                    child: Padding(
                      padding: const EdgeInsets.only(left: 35, right: 30, bottom: 10),
                      child: Container(
                        height: 100,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(20),
                          color: Colors.grey.shade100,
                        ),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.start,
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            const SizedBox(width: 10,),
                            SizedBox(
                              width: 100,
                              height: 100,
                              child: Image.asset('assets/no.png', fit: BoxFit.fill,),
                            ),
                            Column(
                              mainAxisAlignment: MainAxisAlignment.center,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: const [
                                Text('아직까지 데이터가 없어요.'),
                                Text('파이보와 대화를 나누어보세요.'),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ),
                  );
                }

                else{
                  List<String> order = [appState.onlyGood.length.toString(), appState.onlyNorm.length.toString(), appState.onlyBad.length.toString()];
                  List<String> imgIcons = ['assets/sun.png', 'assets/cloud.png', 'assets/rain.png'];
                  List<String> wording = ['행복했', '그냥 그랬', '별로였'];

                  return SizedBox(
                    width: MediaQuery.of(context).size.width * 0.8,
                    height: 330,
                    child: ListView.builder(
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount: 3,
                      itemBuilder: (context, index){
                        return Padding(
                          padding: const EdgeInsets.only(left: 30, right: 30, bottom: 10),
                          child: Container(
                            height: 100,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(20),
                              color: Colors.grey.shade100,
                            ),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.start,
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: [
                                const SizedBox(width: 30,),
                                SizedBox(
                                  width: 100,
                                  height: 100,
                                  child: Image.asset(imgIcons[index], fit: BoxFit.fill,),
                                ),
                                Column(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  crossAxisAlignment: CrossAxisAlignment.start,
                                  children: [
                                    Text('지금까지 ${wording[index]}을 때', style: TextStyle(fontSize: 15,),),
                                    Text('총 ${appState.feelings.length}번 중에 ${order[index]}번', style: TextStyle(fontSize: 15,),),
                                  ],
                                ),
                              ],
                            ),
                          ),
                        );
                      }
                    ),
                  );
                }
              }
            ),
          ],
        ),
      ),
    );
  }
}