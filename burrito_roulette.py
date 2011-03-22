"""
burrito_roulette.py

Copyright 2011 Bump Technologies, Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import pprint, random

burritos = ['al pastor', 'carne asada', 'pollo', 'pollo asado', 'carnitas', 'chile verde', 'chile colorado']
restaurants = [ { 'name' : 'los charros', 'phone' : '650-969-1464'}, {'name' : 'la bamba', 'phone' : '650-965-2755' }, {'name' : ''los portales', 'phone' : '650-968-0453'} ]

def main():
    pprint.pprint((random.choice(burritos), random.choice(restaurants)))

if __name__ == "__main__":
    main()
