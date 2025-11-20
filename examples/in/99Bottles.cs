using System.Collections;

namespace Bottles;

public class Bottles
{
    public string Verse(int verseNumber)
    {
        switch (verseNumber)
        {
            case 0:
                return "No more bottles of beer on the wall, " +
                       "no more bottles of beer.\n" +
                       "Go to the store and buy some more, " +
                       "99 bottles of beer on the wall.";
            case 1:
                return "1 bottle of beer on the wall, " +
                       "1 bottle of beer.\n" +
                       "Take it down and pass it around, " +
                       "no more bottles of beer on the wall.\n";
            case 2:
                return "2 bottles of beer on the wall, " +
                       "2 bottles of beer.\n" +
                       "Take one down and pass it around, " +
                       "1 bottle of beer on the wall.\n";
            default:
                return $"{verseNumber} bottles of beer on the wall, " +
                       $"{verseNumber} bottles of beer.\n" +
                       "Take one down and pass it around, " +
                       $"{verseNumber - 1} bottles of beer on the wall.\n";
        }
    }

    public string Verses(int from, int to)
    {
        var result = new ArrayList();

        for (var i = from; i >= to; i--)
            result.Add(Verse(i));

        return string.Join("\n", result.ToArray());
    }

    public string Song()
    {
        return Verses(99, 0);
    }
}