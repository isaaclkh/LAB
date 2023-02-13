import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:rive/rive.dart';
import 'package:sign_in_button/sign_in_button.dart';

import '../Functions/loginStream.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  late RiveAnimationController _controller;

  void _togglePlay() =>
      setState(() => _controller.isActive = !_controller.isActive);

  /// Tracks if the animation is playing by whether controller is running
  bool get isPlaying => _controller.isActive;

  @override
  void initState() {
    super.initState();
    _controller = SimpleAnimation('idle');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder(
        stream: FirebaseAuth.instance.authStateChanges(),
        builder: (BuildContext context, snapshot) {
          if (snapshot.hasData) {
            WidgetsBinding.instance.addPostFrameCallback((_){
              Navigator.popUntil(context, ModalRoute.withName(Navigator.defaultRouteName));
            });
          } else {
            return Center(
              child: Stack(
                //mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                          width: 200,
                          height: 200,
                          child: const RiveAnimation.asset(
                            'assets/05_eye_rigv02.riv',
                            fit: BoxFit.fill,
                          ),
                        ),
                        const SizedBox(height: 50,),
                        Center(
                          child: SizedBox(
                            height: 30,
                            child: SignInButton(
                              Buttons.googleDark,
                              onPressed: () {
                                LoginStream().signInWithGoogle();
                              },
                            ),
                          ),
                        ),
                        const SizedBox(height: 60,),
                      ]
                  ),
                ],
              ),
            );
          }
          return const Center(child: CircularProgressIndicator(),);
        },
      ),
    );
  }
}