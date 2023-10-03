import 'package:flutter/material.dart';

class Announcement extends StatelessWidget {

  const Announcement({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 351,
      height: 158,


      decoration: const BoxDecoration(
        color: Colors.white,

        boxShadow: [
          BoxShadow(
            color: Colors.black,
            blurRadius: 2.0,
            spreadRadius: 0.0,
            offset: Offset(2.0, 2.0), // shadow direction: bottom right
          )
        ],

        borderRadius: BorderRadius.only(
          bottomLeft: Radius.circular(10),
          bottomRight: Radius.circular(10),
        ),

      ),

      child : Column(
        children : const [
          SizedBox(height : 9),
          AnnouncementRow(info : "(학생식당) 라면 + 마요덮밥 코나 추가 운영", date : "03.27",),
          AnnouncementRow(info : "[학생지원팀]환호여자중학교 1학기 대학생 학습 ...", date : "03.27"),
          AnnouncementRow(info : "[ICT 창업학부]206호 205호 미팅룸 예약 신청 공지", date : "03.27"),
          AnnouncementRow(info : "[총학생회] QT할래? 4월호 배부공지", date : "03.27"),
          AnnouncementRow(info : "[손양원 College] 봄날의 Calling 이벤트 참여", date : "03.27"),
          SizedBox(height : 10),
          Divider(),
          MenuBar(),
        ],
      ),
    );
  }
}

class AnnouncementRow extends StatelessWidget {

  const AnnouncementRow({Key? key, required this.info, required this.date}) : super(key: key);

  final String info;
  final String date;

  @override
  Widget build(BuildContext context) {
    return Row(
      children : [
        const SizedBox(width: 11),
        const Icon(Icons.brightness_1, size: 3,),
        const SizedBox(width: 14),
        Container(
          width : 274,
          child : Text(info, overflow : TextOverflow.ellipsis),
        ),
        const SizedBox(width: 3),
        Text(date),
      ],
    );
  }
}

class MenuBar extends StatelessWidget {

  const MenuBar({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      children : const [
        SizedBox(width: 13,),
        Icon(Icons.subdirectory_arrow_right, size: 13,), // icons 뭔지 몰라서...
        Spacer(),
        Text('전체공지'),
        SizedBox(width: 17,),
      ],
    );
  }
}