import 'package:flutter/cupertino.dart';
import 'package:qr_flutter/qr_flutter.dart';

class QR extends StatelessWidget {
  const QR({Key? key, required this.url}) : super(key: key);

  final String url;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 320,
      height: 320,
      child: Center(
        child: QrImageView(
          data: url,
          version: QrVersions.auto,
          gapless: false,
        ),
      ),
    );
  }
}
