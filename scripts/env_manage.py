#!/usr/bin/env python3
"""Simple .env management helper

Usage:
  python scripts/env_manage.py init      # create .env from .env.example (if missing)
  python scripts/env_manage.py validate  # check required keys are set
  python scripts/env_manage.py show      # show masked values for common keys

This tool uses python-dotenv. Install with: `pip install python-dotenv`
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def init(example: str = '.env.example', target: str = '.env') -> int:
    ex = PROJECT_ROOT / example
    tgt = PROJECT_ROOT / target
    if not ex.exists():
        print(f'Example file {ex} not found.')
        return 1
    if tgt.exists():
        print(f'{tgt} already exists. Aborting to avoid overwrite.')
        return 0
    tgt.write_text(ex.read_text())
    print(f'Created {tgt} from {ex}. Please edit it and fill secrets.')
    return 0


def validate(required_keys=None, target: str = '.env') -> int:
    if required_keys is None:
        required_keys = ['OPENAI_API_KEY']
    env_path = PROJECT_ROOT / target
    if not env_path.exists():
        print(f'{target} not found. Run `init` or create it manually.')
        return 2
    load_dotenv(env_path)
    missing = [k for k in required_keys if not os.getenv(k)]
    if missing:
        print('Missing required keys:', ', '.join(missing))
        return 1
    print('All required keys present.')
    return 0


def show(target: str = '.env') -> int:
    env_path = PROJECT_ROOT / target
    if not env_path.exists():
        print(f'{target} not found.')
        return 2
    load_dotenv(env_path)
    keys = ['OPENAI_API_KEY', 'SECRET_KEY']
    for k in keys:
        v = os.getenv(k, '')
        if v:
            masked = (v[:4] + '...' + v[-4:]) if len(v) > 8 else '***'
        else:
            masked = '<not set>'
        print(f'{k}={masked}')
    return 0


def main():
    if len(sys.argv) < 2:
        print('Usage: python scripts/env_manage.py [init|validate|show]')
        sys.exit(2)
    cmd = sys.argv[1].lower()
    if cmd == 'init':
        sys.exit(init())
    elif cmd == 'validate':
        sys.exit(validate())
    elif cmd == 'show':
        sys.exit(show())
    else:
        print('Unknown command:', cmd)
        sys.exit(2)


if __name__ == '__main__':
    main()
