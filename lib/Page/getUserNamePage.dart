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
    return const Scaffold(
      body: Center(
        child: SizedBox(
          width: 280,
          child: GetTextField(),
        ),
      ),
    );
  }
}
