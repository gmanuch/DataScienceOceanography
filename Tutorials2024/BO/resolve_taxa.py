### code to help run taxa identification for g2 ifcb data through worms web service client and pyworms
### Not robust enough to fully resolve all the taxa, which requires more manual work and likely other databases

import pyworms
from suds import null, WebFault
from suds.client import Client
cl = Client('https://www.marinespecies.org/aphia.php?p=soap&wsdl=1')

# helper function to assign diatom/dino/haptophyte/other
def assign_thru_records(records, genus):
    # loop through records
    for record in records:
        # check if status is accepted or nomen dubium
        if (record['status'] not in ['accepted', 'nomen dubium']):
            # get the valid name
            new_name = record['valid_name']
            # if valid name is same as the original name or doesnt exist, skip to next record
            if (record['scientificname']== record['valid_name']) or (record['valid_name'] is None):
                continue
            # get new record of valid name
            new_records = pyworms.aphiaRecordsByName(new_name, marine_only=False)
            # recursively call function
            gen_group = assign_thru_records(new_records, genus)
            # break out
            break
        # if accepted, is the record on the genus level- assign by phylum level
        # pyworms doesn't return sublevels (ie infraphylum)
        elif (record['rank']=='Genus'):
            # get classifigen_groupions- haptophytes
            if record['phylum']=='Haptophyta':
                gen_group = {genus:'Haptophyte'}
            # diatoms
            elif record['phylum']=='Ochrophyta':
                gen_group = {genus:'Diatom'}
            # dinoflagellate phylum
            elif record['phylum'] == 'Myzozoa':
                gen_group = {genus:'Dinoflagellate'}
            # other- add N-fixers later?
            else:
                gen_group = {genus:'Other'}
        # if not a genus test
        else:
            # go to the next record
            continue
        break
    return(gen_group)

# input takes in a list of unique genuses to search
# output returns list of dictionaries with the assignments found thru worms
def group_assignments(search_list):
    # everything on the genus level
    record_list = []
    genus_list = search_list
    for genus in genus_list:
        # print genus that's being currently searched
        print(genus)
        # get aphia records
        records = pyworms.aphiaRecordsByName(genus, marine_only=False)
        # check if records is none type
        if records is None:
            # try fuzzy matching thru suds (worms python webservice)
            results_array = cl.service.matchAphiaRecordsByNames(genus, fuzzy="true", marine_only="false")
            # just pull first matching record if not none
            if (results_array is not None) and len(results_array[0]) != 0:
                # returns an array, just pull genus first record available
                new_name = results_array[0][0].genus
                # pull records for newly matched genus
                records = pyworms.aphiaRecordsByName(new_name, marine_only=False)
            # if still none, skip the genus in list
            else:
                continue
        # get dict of genus with assigned higher group from original name
        cat = assign_thru_records(records, genus)
        record_list.append(cat)
    return(record_list)
