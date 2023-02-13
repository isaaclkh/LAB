import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pibo/Provider/userProvider.dart';
import 'package:provider/provider.dart';

class GetTextField extends StatefulWidget {
  const GetTextField({Key? key}) : super(key: key);

  @override
  State<GetTextField> createState() => _GetTextFieldState();
}

class _GetTextFieldState extends State<GetTextField> {
  String _name = '';

  final TextEditingController _textController = new TextEditingController();
  @override
  Widget build(BuildContext context) {
    return TextField(
        controller: _textController,
        //obscureText: true,
        decoration: const InputDecoration(
          border: OutlineInputBorder(),
          labelText: '이름을 입력해주세요 (ex. 홍길동)',
        ),
        inputFormatters: <TextInputFormatter>[FilteringTextInputFormatter.allow(RegExp(r'[a-z|A-Z|0-9|ㄱ-ㅎ|ㅏ-ㅣ|가-힣|ᆞ|ᆢ|ㆍ|ᆢ|ᄀᆞ|ᄂᆞ|ᄃᆞ|ᄅᆞ|ᄆᆞ|ᄇᆞ|ᄉᆞ|ᄋᆞ|ᄌᆞ|ᄎᆞ|ᄏᆞ|ᄐᆞ|ᄑᆞ|ᄒᆞ]')),],
        onSubmitted: _onSubmit,
      );
  }
  void _onSubmit(String value) async{
    setState(() => _name = value);
    await context.read<UserProvider>().addUserName(_name);
    Navigator.pushReplacementNamed(context, '/home');
  }
}
