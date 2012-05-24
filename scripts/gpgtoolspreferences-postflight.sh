#!/bin/sh

if test "$USER" == ""
then
  USER=$(id -un)
fi

prefname="GPGPreferences.prefPane"

mkdir -p "$HOME/Library/PreferencePanes/"
chown -R "$USER" "/private/tmp/$prefname" "$HOME/Library/PreferencePanes"
rm -fr "$HOME/Library/PreferencePanes/$prefname"
mv "/private/tmp/$prefname" "$HOME/Library/PreferencePanes/"

exit 0;
