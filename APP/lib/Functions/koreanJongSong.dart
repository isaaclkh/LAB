
class KoreanJongSong{
  KoreanAA(String korean){
    if (KoreanEndsWithJong(korean)){
      return '$korean아';
    }

    else {
      return '$korean';
    }

  }

  KoreanLEE(String korean){
    if (KoreanEndsWithJong(korean)){
      return '$korean이';
    }

    else {
      return '$korean';
    }

  }

  KoreanEndsWithJong(String korean){
    return (korean.runes.last - 0xAC00) % 28!=0;
  }
}

