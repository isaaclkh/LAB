// import 'package:firebase_auth/firebase_auth.dart';
import 'package:pibo/Page/bibleList.dart';
import 'package:pibo/Page/chatting.dart';
import 'package:pibo/Page/getFromPibo.dart';
import 'package:pibo/Page/onBoardingPage.dart';
import 'package:pibo/Provider/appState.dart';
import 'package:provider/provider.dart';
import 'package:pibo/Page/pictures.dart';

import "package:firebase_core/firebase_core.dart";
import "package:flutter/material.dart";
import 'Functions/bottomNavi.dart';
import 'Page/diary.dart';
import 'Page/feeling.dart';
import 'Page/getUserNamePage.dart';
import 'Page/home.dart';
import 'Provider/productProvider.dart';
import 'Provider/userProvider.dart';
import 'firebase_options.dart';


String userName = '';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => UserProvider()),
        ChangeNotifierProvider(create: (_) => ProductProvider()),
        ChangeNotifierProvider(create: (_) => ApplicationState()),
      ],
      child: const MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {

    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => UserProvider()),
        ChangeNotifierProvider(create: (_) => ProductProvider()),
        ChangeNotifierProvider(create: (_) => ApplicationState()),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: "Pibo",
        theme: ThemeData(
        primaryColor: Colors.lightBlueAccent,
        fontFamily: 'Spoqa',
        backgroundColor: Colors.white,
        ),
        home: const OnBoardingPage(),
        // LoginStream().handleAuthState(),
        // ProfilePage(),

        initialRoute: '/',
        routes: {
          // '/splash/init': (context) => const InitPage(),
          '/bibleList': (context) => const BibleList(),
          '/pictures': (context) => const Pictures(),
          '/home': (context) => const HomePage(),
          '/diary': (context) => const Diary(),
          '/feeling': (context) => const Feeling(),
          '/initial' : (context) => const BottomNavi(),
          '/onboarding' : (context) => const OnBoardingPage(),
          '/username' : (context) => const GetUserNamePage(),
          '/chatting' : (context) => const Chatting(),
          '/fromPibo' : (context) => const GetFromPibo(),
        },
      ),
    );
  }
}
