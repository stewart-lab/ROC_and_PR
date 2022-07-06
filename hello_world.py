import cmdlogtime
import sys

COMMAND_LINE_DEF_FILE = "fan_collab_cmdlogtime_deck.txt"


def main():
    pass


if __name__ == "__main__":
    # Call cmdlogtime.begin() at the beginning of main()
    (start_time_secs, pretty_start_time, my_args, logfile) = cmdlogtime.begin(
        COMMAND_LINE_DEF_FILE, sys.argv[0]
    )

    # the command line arguments will be in the my_args dictionary returned. 
    # Access them like this:
    # get_treats_vectors = my_args["get_treats_vectors"]

    #  Then you put all of your code here.....
    main()

    # if you want to add stuff to the logfile:
    logfile.write("Hello World")

    # The only functions you probably will ever need in cmdlogtime are 
    # begin(), end(), and maybe make_dir. Here's an example:
    # cmdlogtime.make_dir(intermediate_out_dir)

    # Call cmdlogtime.end() at the end of main()
    cmdlogtime.end(logfile, start_time_secs)

