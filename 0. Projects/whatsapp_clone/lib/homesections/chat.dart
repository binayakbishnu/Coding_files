import 'package:flutter/material.dart';

class Chat extends StatelessWidget {
  const Chat({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        // content
        Row(
            mainAxisAlignment: MainAxisAlignment.start,
            // crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              // profile pic
              Container(
                width: 56,
                height: 56,
                decoration: const BoxDecoration(
                  color: Colors.blueGrey,
                  borderRadius:
                  BorderRadius.all(Radius.circular(28)),
                ),
              ),
              const SizedBox(
                width: 20,
              ),
              // name and message
              Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Text(
                    'Binayak Bishnu',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      color:
                      Theme.of(context).colorScheme.onPrimary,
                    ),
                  ),
                  const SizedBox(
                    height: 3,
                  ),
                  Text(
                    'Sent you a new message',
                    style: TextStyle(
                      color: Theme.of(context)
                          .colorScheme
                          .onBackground,
                    ),
                  ),
                ],
              ),
            ]),

        // msg notifications
        Column(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: <Widget>[
            Text(
              '12:45 pm',
              style: TextStyle(
                  color: Theme.of(context).colorScheme.primary,
                  fontWeight: FontWeight.bold,
                  fontSize: 13.0),
            ),
            const SizedBox(
              height: 3,
            ),
            Row(
              children: [
                Icon(
                  Icons.crisis_alert,
                  color: Theme.of(context).colorScheme.error,
                  size: 20,
                ),
                const SizedBox(
                  width: 5,
                ),
                Container(
                  width: 20,
                  height: 20,
                  decoration: BoxDecoration(
                    color: Theme.of(context).colorScheme.primary,
                    borderRadius:
                    const BorderRadius.all(Radius.circular(13)),
                  ),
                  child: const Center(
                    child: Text(
                      '5',
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                        fontSize: 10.0,
                      ),
                    ),
                  ),
                ),
                const SizedBox(
                  width: 5,
                ),
                Icon(
                  Icons.pin_drop_sharp,
                  color: Theme.of(context).colorScheme.onBackground,
                  size: 20,
                ),
              ],
            ),
          ],
        ),
      ],
    );
  }
}
