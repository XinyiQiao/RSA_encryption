# -*- coding: utf-8 -*-

'''
cli
---

console script for rsa_encryption.
'''


import click
import sys

from .rsa_encryption import generate_prime

@click.group()
@click.pass_context
@click.option(
'--n',
required = True,
type = int,
default='1024',
help = "bit-size for prime number"
)
def main(ctx,n):
    '''
    RSA_encryption command line interface
    '''

    ctx.obj['n']=n

@main.command()
@click.pass_context
def prime_generator(ctx):

    generate_prime(ctx.obj['n'])


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main(obj={}))  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
