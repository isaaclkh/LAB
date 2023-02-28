import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:provider/provider.dart';

import '../main.dart';

class GetTextField extends StatefulWidget {
  const GetTextField({Key? key}) : super(key: key);

  @override
  State<GetTextField> createState() => _GetTextFieldState();

  String getName() {
    return _GetTextFieldState()._name;
  }
}

class _GetTextFieldState extends State<GetTextField> {
  String _name = '';

  final TextEditingController _textController = new TextEditingController();
  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: _textController,
      style: const TextStyle(color: Colors.white,),
      //obscureText: true,
      decoration: const InputDecoration(

        enabledBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.white, width: 1, ),
        ),
        focusedBorder: OutlineInputBorder(
          borderSide: BorderSide(color: Colors.lightBlueAccent, width: 1, ),
        ),

        labelText: '이름을 입력해주세요 (ex. 홍길동)',
        labelStyle: TextStyle(color: Colors.white),
      ),

      inputFormatters: <TextInputFormatter>[
        FilteringTextInputFormatter.allow(
          RegExp(
              r'[a-z|A-Z|0-9|ㄱ-ㅎ|ㅏ-ㅣ|가-힣|ᆞ|ᆢ|ㆍ|ᆢ|ᄀᆞ|ᄂᆞ|ᄃᆞ|ᄅᆞ|ᄆᆞ|ᄇᆞ|ᄉᆞ|ᄋᆞ|ᄌᆞ|ᄎᆞ|ᄏᆞ|ᄐᆞ|ᄑᆞ|ᄒᆞ]'
          ),
        ),
      ],

      onSubmitted: _onSubmit,
    );
  }

  void _onSubmit(String value) async{

    if(value.length >= 3){
      value = value.substring(value.length-2);
    }

    setState(() => _name = value);
    setState(() => userName = value);
    await context.read<UserProvider>().addUserName(_name);
    Navigator.pushReplacementNamed(context, '/home', arguments: _name);
  }

}