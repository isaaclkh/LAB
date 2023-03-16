import 'package:flutter/cupertino.dart';
import 'package:ionicons/ionicons.dart';

class FeelIcon{
  howDoYouFeel(String f){
    if(f.contains('GOOD')){
      return const Icon(Ionicons.sunny_outline);
    }

    if(f.contains('NORMAL')){
      return const Icon(Ionicons.partly_sunny_outline);
    }

    if(f.contains('BAD')){
      return const Icon(Ionicons.thunderstorm_outline);
    }
  }

}
