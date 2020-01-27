/*
   BAREOS® - Backup Archiving REcovery Open Sourced

   Copyright (C) 2020-2020 Bareos GmbH & Co. KG

   This program is Free Software; you can redistribute it and/or
   modify it under the terms of version three of the GNU Affero General Public
   License as published by the Free Software Foundation and included
   in the file LICENSE.

   This program is distributed in the hope that it will be useful, but
   WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
   Affero General Public License for more details.

   You should have received a copy of the GNU Affero General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
   02110-1301, USA.
*/

#ifndef BAREOS_SRC_DIRD_DBCONVERT_DATABASE_IMPORTER_H_
#define BAREOS_SRC_DIRD_DBCONVERT_DATABASE_IMPORTER_H_

#include <map>
#include <string>

class BareosDb;
class DatabaseConnection;
class DatabaseExport;
class DatabaseTableDescriptions;

class DatabaseImport {
 public:
  DatabaseImport(const DatabaseConnection& db_connection);
  virtual ~DatabaseImport();

  void ExportTo(DatabaseExport& exporter);

 private:
  BareosDb* db_{};

  std::unique_ptr<DatabaseTableDescriptions> table_descriptions_;
  static int ResultHandler(void* ctx, int fields, char** row);
};


#endif  // BAREOS_SRC_DIRD_DBCONVERT_DATABASE_IMPORTER_H_
