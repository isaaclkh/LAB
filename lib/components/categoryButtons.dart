import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class CategoryButtons extends StatelessWidget {
  final String where;
  final String buttonName;
  final IconData buttonIcon;

  const CategoryButtons({Key? key, required this.where, required this.buttonName, required this.buttonIcon}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        minimumSize: Size(150,100),
      ),
      onPressed: (){
        Navigator.pushNamed(context, where);
      },
      child: SizedBox(
        height: 100,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(buttonIcon),
            const SizedBox(height: 15,),
            Text(buttonName),
          ],
        ),
      ),
    );
  }
}
