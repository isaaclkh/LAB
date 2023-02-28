import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/components/getTextField.dart';

class GetUserNamePage extends StatefulWidget {
  const GetUserNamePage({Key? key}) : super(key: key);

  @override
  State<GetUserNamePage> createState() => _GetUserNamePageState();
}

class _GetUserNamePageState extends State<GetUserNamePage> {
  @override
  Widget build(BuildContext context) {
    return Container(
      //width: MediaQuery.of(context).size.width,
      //height: MediaQuery.of(context).size.height,
      decoration: const BoxDecoration(
        image: DecorationImage(
          fit: BoxFit.cover,
          image: AssetImage('assets/bgIm.jpg'),
        )
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent.withOpacity(0.3),
        body: SizedBox(
          width: MediaQuery.of(context).size.width,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Image.asset('assets/logo.png', width: 230,),
              const SizedBox(height: 40,),
              const SizedBox(
                width: 280,
                child: GetTextField(),
              ),
              const SizedBox(height: 70,),
            ],
          ),
        ),
      ),
    );
  }
}
