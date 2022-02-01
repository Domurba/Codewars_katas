#2021-11-30 10:04:32.131000+00:00
"""<style>
  .recursive-heading {
    background-color: #c0c0c0;
    color: #131414;
    text-align: center;
    padding: 10px;
  }

  .recursive-heading div:first-child {
    font-size: 25px
  }

  .recursive-heading div:last-child {
    margin-top: 10px
  }

  .recursive-heading div span {
    color: black;
    cursor: pointer;
    text-decoration: underline;
  }

  .recursive-footer {
    text-align: center;
    padding: 10px 0;
  }
  
  .recursive-footer span {
    font-weight: bold;
  }

  .recursive-footer .next {
    float: right;
  }

  .recursive-footer .previous {
    float: left;
  }

  .recursive-footer .previous i {
    display: inline-block;
    -webkit-transform: rotate(180deg);
    -moz-transform: rotate(180deg);
    -o-transform: rotate(180deg);
    -ms-transform: rotate(180deg);
    transform: rotate(180deg);
  }

  .clear {
    clear: both;
  }
</style>

<div class="recursive-heading">
  <div><i class="icon-moon-bookmark is-large"></i>
  Do you know <span>recursion</span>?</div>
  <div>This is a kata series that you can only solve using recursion.</div>
</div>

#\#1 - Factorial

In mathematics, the <a href="https://en.wikipedia.org/wiki/Factorial" target="_blank">factorial</a> of a non-negative integer `n`, denoted by `n!`, is the product of all positive integers less than or equal to `n`. For example,

`5! = 5 * 4 * 3 * 2 * 1 = 120.`

The value of `0!` is `1`.

#Your task

You have to create the function `factorial` that receives `n` and returns `n!`. You have to use recursion.

<div class="recursive-footer">
  <a class="btn is-alt next" href="http://www.codewars.com/kata/recursion-number-2-fibonacci">
    <i class="icon-moon-next"></i>Next (<span>Recursion #2 - Fibonacci</span>)
  </a>
  <div class="clear"></div>
</div>"""

WITH RECURSIVE factorial as (
  SELECT 0 as n, 1::bigint as fact
UNION ALL
SELECT n + 1, ((n +1) * fact)::bigint
FROM factorial
  where n < 16
)
SELECT * from factorial;

