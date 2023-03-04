#!/usr/bin/perl
$M = {
    "integer number" => "integer",
        "free text" => "string",
        "CC-Sss" => "string",
};
while(<>) {
    @parts = split(/\t/, $_);
    $u = $parts[2];
    my $rng = "float";
    if ($u eq "Units") {
        $rng = "Range";
    }
    elsif ($u =~ m@LIST\((.*)\)@) {
        $rng = $1;
        $u = "";
    }
    elsif ($M->{$u}) {
        $rng = $M->{$u};
        $u = "";
    }
    splice(@parts, 2, 1, ($rng, $u));
    print join("\t", @parts);
}
