# laggy

Laggy lets you securely and anonymously communicate using small voice messages.

The current code is a simple proof of concept.

## "quick" start

This assumes some comfort in configuring tor hidden services.

After cloning this repo, configure a hidden service for laggy. On ubuntu, adding the following to /etc/tor/torrc will work:

    HiddenServiceDir /var/lib/tor/laggy/
    HiddenServicePort 80 127.0.0.1:9998

Ensure your control port is configured as well. Restart or HUP tor, and ensure you have a hostname in the hidden service directory you just configured.

Next, edit config.yml to reflect your situation. Importantly, you'll want to update the `hostname` attribute to be the hostname of the service you just configured. Depending on if you're using TBB or just normal tor, you may have to update the proxy port.

Laggy requires a number of python packages, including pyaudio, socks, PyYAML, cyclone, and txsocksx. On debian, `sudo apt-get install python-pyaudio python-socksipy python-yaml python-cyclone` will get you started. PyYAML and txsocksx might be better installed via pip.

## running

Once you're all configured, laggy can be started with:

    ./laggy.py --config conf.yaml <peer-url.onion>

At the moment, peer discover is done out-of-band: you must exchange your service address with your peer before you can communicate using laggy.

Once laggy starts, usage is simple: start recording a message by pressing the space bar. Stop recording by pressing the space bar again. When you stop recording, the message is sent automatically to your peer.
