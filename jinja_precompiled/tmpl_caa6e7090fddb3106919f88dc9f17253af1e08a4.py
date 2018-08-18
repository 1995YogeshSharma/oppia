from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'domain/objects/NumberWithUnitsObjectFactory.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2018 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Factory for creating instances of NumberWithUnits and Units\n * domain objects.\n */\n\noppia.constant(\'NUMBER_WITH_UNITS_PARSING_ERRORS\', {\n  INVALID_VALUE:\n    \'Please ensure that value is either a fraction or a number\',\n  INVALID_CURRENCY:\n    \'Please enter a valid currency (e.g., $5 or Rs 5)\',\n  INVALID_CURRENCY_FORMAT: \'Please write currency units at the beginning\',\n  INVALID_UNIT_CHARS:\n    \'Please ensure that unit only contains numbers, alphabets, (, ), *, ^, /, -\'\n});\n\n/* Guidelines for adding new custom currency units in Number with Units\n  interaction:\n\n  Simply add currency unit to the dict of CURRENCY_UNITS constant and it will\n  be automatically added to the allowed custom units. Following are the keys\n  to be defined within the unit dict:\n    name:  The name of the custom currency unit.\n    aliases: Other allowed canonical forms of the currency unit.\n    front_units: A list of all the currency symbols that are added to the front\n      (like- $, Rs, \u20b9). Keep it an empty list if no symbol is needed.\n    base_unit: Define the unit in terms of base unit only if the defined custom\n      unit is a sub unit else assign it \'null\' value.*/\noppia.constant(\'CURRENCY_UNITS\', {\n  dollar: {\n    name: \'dollar\',\n    aliases: [\'$\', \'dollars\', \'Dollars\', \'Dollar\', \'USD\'],\n    front_units: [\'$\'],\n    base_unit: null\n  },\n  rupee: {\n    name: \'rupee\',\n    aliases: [\'Rs\', \'rupees\', \'\u20b9\', \'Rupees\', \'Rupee\'],\n    front_units: [\'Rs \', \'\u20b9\'],\n    base_unit: null\n  },\n  cent: {\n    name: \'cent\',\n    aliases: [\'cents\', \'Cents\', \'Cent\'],\n    front_units: [],\n    base_unit: \'0.01 dollar\'\n  },\n  paise: {\n    name: \'paise\',\n    aliases: [\'paisa\', \'Paise\', \'Paisa\'],\n    front_units: [],\n    base_unit: \'0.01 rupee\'\n  }\n});\n\noppia.factory(\'NumberWithUnitsObjectFactory\', [\n  \'UnitsObjectFactory\', \'FractionObjectFactory\', \'CURRENCY_UNITS\',\n  \'NUMBER_WITH_UNITS_PARSING_ERRORS\', function(\n      UnitsObjectFactory, FractionObjectFactory, CURRENCY_UNITS,\n      NUMBER_WITH_UNITS_PARSING_ERRORS) {\n    var NumberWithUnits = function(type, real, fractionObj, unitsObj) {\n      this.type = type;\n      this.real = real;\n      this.fraction = fractionObj;\n      this.units = unitsObj.units;\n    };\n\n    NumberWithUnits.prototype.toString = function() {\n      var numberWithUnitsString = \'\';\n      var unitsString = UnitsObjectFactory.fromList(this.units).toString();\n      if (unitsString.includes(\'$\')) {\n        unitsString = unitsString.replace(\'$\', \'\');\n        numberWithUnitsString += \'$\' + \' \';\n      }\n      if (unitsString.includes(\'Rs\')) {\n        unitsString = unitsString.replace(\'Rs\', \'\');\n        numberWithUnitsString += \'Rs\' + \' \';\n      }\n      if (unitsString.includes(\'\u20b9\')) {\n        unitsString = unitsString.replace(\'\u20b9\', \'\');\n        numberWithUnitsString += \'\u20b9\' + \' \';\n      }\n\n      if (this.type === \'real\') {\n        numberWithUnitsString += this.real + \' \';\n      } else if (this.type === \'fraction\') {\n        numberWithUnitsString += this.fraction.toString() + \' \';\n      }\n      numberWithUnitsString += unitsString.trim();\n      numberWithUnitsString = numberWithUnitsString.trim();\n\n      return numberWithUnitsString;\n    };\n\n    NumberWithUnits.prototype.toMathjsCompatibleString = function() {\n      var numberWithUnitsString = \'\';\n      var unitsString = UnitsObjectFactory.fromList(this.units).toString();\n      unitsString = UnitsObjectFactory.toMathjsCompatibleString(unitsString);\n\n      if (this.type === \'real\') {\n        numberWithUnitsString += this.real + \' \';\n      } else if (this.type === \'fraction\') {\n        numberWithUnitsString += this.fraction.toString() + \' \';\n      }\n      numberWithUnitsString += unitsString.trim();\n      numberWithUnitsString = numberWithUnitsString.trim();\n\n      return numberWithUnitsString;\n    };\n\n    NumberWithUnits.prototype.toDict = function() {\n      return {\n        type: this.type,\n        real: this.real,\n        fraction: this.fraction.toDict(),\n        units: this.units\n      };\n    };\n\n    NumberWithUnits.createCurrencyUnits = function() {\n      try {\n        Units.createCurrencyUnits();\n      } catch (parsingError) {}\n    };\n\n    NumberWithUnits.fromRawInputString = function(rawInput) {\n      rawInput = rawInput.trim();\n      var type = \'\';\n      var real = 0.0;\n      // Default fraction value.\n      var fractionObj = FractionObjectFactory.fromRawInputString(\'0/1\');\n      var units = \'\';\n      var value = \'\';\n      var unitObj = [];\n\n      // Allow validation only when rawInput is not null or an empty string.\n      if (rawInput !== \'\' && rawInput !== null) {\n        // Start with digit when there is no currency unit.\n        if (rawInput.match(/^\\d/)) {\n          var ind = rawInput.indexOf(rawInput.match(/[a-z(\u20b9$]/i));\n          if (ind === -1) {\n            // There is value with no units.\n            value = rawInput;\n            units = \'\';\n          } else {\n            value = rawInput.substr(0, ind).trim();\n            units = rawInput.substr(ind).trim();\n          }\n\n          var keys = Object.keys(CURRENCY_UNITS);\n          for (var i = 0; i < keys.length; i++) {\n            for (var j = 0;\n              j < CURRENCY_UNITS[keys[i]].front_units.length; j++) {\n              if (units.indexOf(\n                CURRENCY_UNITS[keys[i]].front_units[j]) !== -1) {\n                throw new Error(\n                  NUMBER_WITH_UNITS_PARSING_ERRORS.INVALID_CURRENCY_FORMAT);\n              }\n            }\n          }\n        } else {\n          var startsWithCorrectCurrencyUnit = false;\n          var keys = Object.keys(CURRENCY_UNITS);\n          for (var i = 0; i < keys.length; i++) {\n            for (var j = 0;\n              j < CURRENCY_UNITS[keys[i]].front_units.length; j++) {\n              if (rawInput.startsWith(CURRENCY_UNITS[keys[i]].front_units[j])) {\n                startsWithCorrectCurrencyUnit = true;\n                break;\n              }\n            }\n          }\n          if (startsWithCorrectCurrencyUnit === false) {\n            throw new Error(NUMBER_WITH_UNITS_PARSING_ERRORS.INVALID_CURRENCY);\n          }\n          var ind = rawInput.indexOf(rawInput.match(/[0-9]/));\n          if (ind === -1) {\n            throw new Error(NUMBER_WITH_UNITS_PARSING_ERRORS.INVALID_CURRENCY);\n          }\n          units = rawInput.substr(0, ind).trim();\n\n          startsWithCorrectCurrencyUnit = false;\n          for (var i = 0; i < keys.length; i++) {\n            for (var j = 0;\n              j < CURRENCY_UNITS[keys[i]].front_units.length; j++) {\n              if (units === CURRENCY_UNITS[keys[i]].front_units[j].trim()) {\n                startsWithCorrectCurrencyUnit = true;\n                break;\n              }\n            }\n          }\n          if (startsWithCorrectCurrencyUnit === false) {\n            throw new Error(NUMBER_WITH_UNITS_PARSING_ERRORS.INVALID_CURRENCY);\n          }\n          units = units + \' \';\n\n          var ind2 = rawInput.indexOf(\n            rawInput.substr(ind).match(/[a-z(]/i));\n          if (ind2 !== -1) {\n            value = rawInput.substr(ind, ind2 - ind).trim();\n            units += rawInput.substr(ind2).trim();\n          } else {\n            value = rawInput.substr(ind).trim();\n            units = units.trim();\n          }\n        }\n        // Checking invalid characters in value.\n        if (value.match(/[a-z]/i) || value.match(/[*^$\u20b9()#@]/)) {\n          throw new Error(NUMBER_WITH_UNITS_PARSING_ERRORS.INVALID_VALUE);\n        }\n\n        if (value.includes(\'/\')) {\n          type = \'fraction\';\n          fractionObj = FractionObjectFactory.fromRawInputString(value);\n        } else {\n          type = \'real\';\n          real = parseFloat(value);\n        }\n        if (units !== \'\') {\n          // Checking invalid characters in units.\n          if (units.match(/[^0-9a-z/* ^()\u20b9$-]/i)) {\n            throw new Error(\n              NUMBER_WITH_UNITS_PARSING_ERRORS.INVALID_UNIT_CHARS);\n          }\n        }\n      }\n\n      unitsObj = UnitsObjectFactory.fromRawInputString(units);\n      return new NumberWithUnits(type, real, fractionObj, unitsObj);\n    };\n\n    NumberWithUnits.fromDict = function(numberWithUnitsDict) {\n      return new NumberWithUnits(\n        numberWithUnitsDict.type,\n        numberWithUnitsDict.real,\n        FractionObjectFactory.fromDict(numberWithUnitsDict.fraction),\n        UnitsObjectFactory.fromList(numberWithUnitsDict.units));\n    };\n\n    return NumberWithUnits;\n  }\n]);\n\noppia.factory(\'UnitsObjectFactory\', [\'CURRENCY_UNITS\',\n  function(CURRENCY_UNITS) {\n    var Units = function(unitsList) {\n      this.units = unitsList;\n    };\n\n    var isunit = function(unit) {\n      return !(\'/*() \'.includes(unit));\n    };\n\n    Units.stringToLexical = function(units) {\n      units += \'#\';\n      var unitList = [];\n      var unit = \'\';\n      for (var i = 0; i < units.length; i++) {\n        if (\'*/()# \'.includes(units[i]) && unit !== \'per\') {\n          if (unit.length > 0) {\n            if ((unitList.length > 0) && isunit(unitList.slice(-1).pop())) {\n              unitList.push(\'*\');\n            }\n            unitList.push(unit);\n            unit = \'\';\n          }\n          if (!(\'# \'.includes(units[i]))) {\n            unitList.push(units[i]);\n          }\n        } else if (units[i] === \' \' && unit === \'per\') {\n          unitList.push(\'/\');\n          unit = \'\';\n        } else {\n          unit += units[i];\n        }\n      }\n      return unitList;\n    };\n\n    var unitWithMultiplier = function(unitList) {\n      var multiplier = 1;\n      var unitsWithMultiplier = [];\n      var parenthesisStack = [];\n\n      for (var ind = 0; ind < unitList.length; ind++) {\n        if (unitList[ind] === \'/\') {\n          multiplier = -multiplier;\n        } else if (unitList[ind] === \'(\') {\n          if (unitList[ind - 1] === \'/\') {\n            // If previous element was division then we need to inverse\n            // multiplier when we find its corresponsing closing parenthesis.\n            // Second element of pushed element is used for this purpose.\n            parenthesisStack.push([\'(\', -1]);\n          } else {\n            // If previous element was not division then we don\'t need to\n            // invert the multiplier.\n            parenthesisStack.push([\'(\', 1]);\n          }\n        } else if (unitList[ind] === \')\') {\n          var elem = parenthesisStack.pop();\n          multiplier = parseInt(elem[1]) * multiplier;\n        } else if (isunit(unitList[ind])) {\n          unitsWithMultiplier.push([unitList[ind], multiplier]);\n          // If previous element was division then we need to invert\n          // multiplier.\n          if (unitList[ind - 1] === \'/\') {\n            multiplier = -multiplier;\n          }\n        }\n      }\n      return unitsWithMultiplier;\n    };\n\n    var convertUnitDictToList = function(unitDict) {\n      var unitList = [];\n      for (var key in unitDict) {\n        unitList.push({unit: key, exponent: unitDict[key]});\n      }\n      return unitList;\n    };\n\n    var unitToList = function(unitsWithMultiplier) {\n      var unitDict = {};\n      for (var i = 0; i < unitsWithMultiplier.length; i++) {\n        var unit = unitsWithMultiplier[i][0];\n        var multiplier = unitsWithMultiplier[i][1];\n        var ind = unit.indexOf(\'^\');\n        if (ind > -1) {\n          var s = unit.substr(0, ind);\n          var power = parseInt(unit.substr(ind + 1));\n        } else {\n          var s = unit;\n          var power = 1;\n        }\n        if (!(s in unitDict)) {\n          unitDict[s] = 0;\n        }\n        unitDict[s] += multiplier * power;\n      }\n      return convertUnitDictToList(unitDict);\n    };\n\n    Units.prototype.toDict = function() {\n      return {\n        units: this.units\n      };\n    };\n\n    Units.fromList = function(unitsList) {\n      return new Units(unitsList);\n    };\n\n    Units.fromStringToList = function(unitsString) {\n      return unitToList(unitWithMultiplier(Units.stringToLexical(unitsString)));\n    };\n\n    Units.prototype.toString = function() {\n      var unit = \'\';\n      for (var i = 0; i < this.units.length; i++) {\n        var d = this.units[i];\n        if (d.exponent === 1) {\n          unit += d.unit + \' \';\n        } else {\n          unit += d.unit + \'^\' + d.exponent.toString() + \' \';\n        }\n      }\n      return unit.trim();\n    };\n\n    Units.createCurrencyUnits = function() {\n      // Creates user-defined currency (base + sub) units.\n      var keys = Object.keys(CURRENCY_UNITS);\n      for (var i = 0; i < keys.length; i++) {\n        if (CURRENCY_UNITS[keys[i]].base_unit === null) {\n          // Base unit (like: rupees, dollar etc.).\n          math.createUnit(CURRENCY_UNITS[keys[i]].name, {\n            aliases: CURRENCY_UNITS[keys[i]].aliases});\n        } else {\n          // Sub unit (like: paise, cents etc.).\n          math.createUnit(CURRENCY_UNITS[keys[i]].name, {\n            definition: CURRENCY_UNITS[keys[i]].base_unit,\n            aliases: CURRENCY_UNITS[keys[i]].aliases});\n        }\n      }\n    };\n\n    Units.toMathjsCompatibleString = function(units) {\n      // Makes the units compatible with the math.js allowed format.\n      units = units.replace(/per/g, \'/\');\n\n      // Special symbols need to be replaced as math.js doesn\'t support custom\n      // units starting with special symbols. Also, it doesn\'t allow units\n      // followed by a number as in the case of currency units.\n      var keys = Object.keys(CURRENCY_UNITS);\n      for (var i = 0; i < keys.length; i++) {\n        for (var j = 0; j < CURRENCY_UNITS[keys[i]].front_units.length; j++) {\n          if (units.includes(CURRENCY_UNITS[keys[i]].front_units[j])) {\n            units = units.replace(CURRENCY_UNITS[keys[i]].front_units[j], \'\');\n            units = CURRENCY_UNITS[keys[i]].name + units;\n          }\n        }\n\n        for (var j = 0; j < CURRENCY_UNITS[keys[i]].aliases.length; j++) {\n          if (units.includes(CURRENCY_UNITS[keys[i]].aliases[j])) {\n            units = units.replace(CURRENCY_UNITS[keys[i]].aliases[j],\n              CURRENCY_UNITS[keys[i]].name);\n          }\n        }\n      }\n      return units.trim();\n    };\n\n    Units.fromRawInputString = function(units) {\n      try {\n        Units.createCurrencyUnits();\n      } catch (parsingError) {}\n\n      compatibleUnits = Units.toMathjsCompatibleString(units);\n      if (compatibleUnits !== \'\') {\n        try {\n          math.unit(compatibleUnits);\n        } catch (err) {\n          throw new Error(err);\n        }\n      }\n      return new Units(Units.fromStringToList(units));\n    };\n\n    return Units;\n  }]);'

blocks = {}
debug_info = ''