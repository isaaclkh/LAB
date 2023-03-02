import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:pibo/Page/feeling.dart';
import 'package:pibo/Provider/productProvider.dart';

class CategoryButtons extends StatelessWidget {
  final String where;
  final String buttonName;
  final IconData buttonIcon;

  const CategoryButtons({Key? key, required this.where, required this.buttonName, required this.buttonIcon}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        minimumSize: Size(140,170),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(18),
        ),
      ),
      onPressed: (){
        Navigator.pushNamed(context, where);
      },
      child: SizedBox(
        height: 100,
        width: 100,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Icon(buttonIcon,size: 45,),
            Spacer(),
            Row(
              children: [
                const SizedBox(width: 6,),
                Text(buttonName),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
